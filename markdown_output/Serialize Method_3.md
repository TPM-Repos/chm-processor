       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Serialize Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4946.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectVariable Class](topic4927.md) : Serialize Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_writer_
    The System.Xml.XmlWriter to serialize this variable to.

Glossary Item Box

Serializes this [ProjectVariable](topic4927.md) to the provided System.Xml.XmlWriter. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Serialize( _
       ByVal _writer_ As XmlWriter _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectVariable](topic4927.md)
    Dim writer As XmlWriter
     
    instance.Serialize(writer)  
  
C#|   
---|---  
      
    
    public void Serialize( 
       XmlWriter _writer_
    )  
  
#### Parameters

 _writer_
    The System.Xml.XmlWriter to serialize this variable to.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectVariable Class](topic4927.md)   
[ProjectVariable Members](topic4928.md)

©2024 DriveWorks Ltd. All Rights Reserved.
