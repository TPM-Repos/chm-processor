Serialize Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlBase Class](topic7698.md) : Serialize Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_writer_
    The XML writer to which to write the serialized control data.

_options_
    Options which configure the serialization process.

Glossary Item Box

Serializes the control and any contents to the given XML writer. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Serialize( _
       ByVal _writer_ As XmlWriter, _
       ByVal _options_ As [SerializationMode](topic7318.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ControlBase](topic7698.md)
    Dim writer As XmlWriter
    Dim options As [SerializationMode](topic7318.md)
     
    instance.Serialize(writer, options)  
  
C#|   
---|---  
      
    
    public void Serialize( 
       XmlWriter _writer_ ,
       [SerializationMode](topic7318.md) _options_
    )  
  
#### Parameters

 _writer_
    The XML writer to which to write the serialized control data.
_options_
    Options which configure the serialization process.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ControlBase Class](topic7698.md)   
[ControlBase Members](topic7699.md)


