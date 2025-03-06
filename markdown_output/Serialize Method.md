       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Serialize Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11441.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationMacro Class](topic11429.md) : Serialize Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_writer_
    The System.Xml.XmlWriter to serialize this macro to.

Glossary Item Box

Serializes this [SpecificationMacro](topic11429.md) to the provided System.Xml.XmlWriter. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Serialize( _
       ByVal _writer_ As XmlWriter _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationMacro](topic11429.md)
    Dim writer As XmlWriter
     
    instance.Serialize(writer)  
  
C#|   
---|---  
      
    
    public void Serialize( 
       XmlWriter _writer_
    )  
  
#### Parameters

 _writer_
    The System.Xml.XmlWriter to serialize this macro to.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationMacro Class](topic11429.md)   
[SpecificationMacro Members](topic11430.md)

©2024 DriveWorks Ltd. All Rights Reserved.
