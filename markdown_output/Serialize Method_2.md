Serialize Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectConstant Class](topic4171.md) : Serialize Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_writer_
    The System.Xml.XmlWriter to serialize this constant to.

Glossary Item Box

Serializes this [ProjectConstant](topic4171.md) to the provided System.Xml.XmlWriter. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Serialize( _
       ByVal _writer_ As XmlWriter _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectConstant](topic4171.md)
    Dim writer As XmlWriter
     
    instance.Serialize(writer)  
  
C#|   
---|---  
      
    
    public void Serialize( 
       XmlWriter _writer_
    )  
  
#### Parameters

 _writer_
    The System.Xml.XmlWriter to serialize this constant to.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectConstant Class](topic4171.md)   
[ProjectConstant Members](topic4172.md)


