       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SerializeCore Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7694.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ContainerControlBase Class](topic7684.md) : SerializeCore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_writer_
    The writer to which to write the serialized control contents.

_options_
    Options which configure the serialization process.

Glossary Item Box

Overridden to serialize child controls. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overrides Sub SerializeCore( _
       ByVal _writer_ As XmlWriter, _
       ByVal _options_ As [SerializationMode](topic7318.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ContainerControlBase](topic7684.md)
    Dim writer As XmlWriter
    Dim options As [SerializationMode](topic7318.md)
     
    instance.SerializeCore(writer, options)  
  
C#|   
---|---  
      
    
    protected override void SerializeCore( 
       XmlWriter _writer_ ,
       [SerializationMode](topic7318.md) _options_
    )  
  
#### Parameters

 _writer_
    The writer to which to write the serialized control contents.
_options_
    Options which configure the serialization process.

# Remarks

See the [ControlBase.SerializeCore](topic7719.md) method for more information.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ContainerControlBase Class](topic7684.md)   
[ContainerControlBase Members](topic7685.md)

©2024 DriveWorks Ltd. All Rights Reserved.
