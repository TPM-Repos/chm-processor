       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Save Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11147.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [RuleResults Class](topic11136.md) : Save Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_writer_
    

Glossary Item Box

Saves the rule results to the specified XML writer. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Save( _
       ByVal _writer_ As XmlWriter _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RuleResults](topic11136.md)
    Dim writer As XmlWriter
     
    instance.Save(writer)  
  
C#|   
---|---  
      
    
    public void Save( 
       XmlWriter _writer_
    )  
  
#### Parameters

 _writer_
    

# Remarks

Rule results are saved using the specification XML namespace (http://schemas.driveworks.co.uk/specification/)

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RuleResults Class](topic11136.md)   
[RuleResults Members](topic11137.md)

©2024 DriveWorks Ltd. All Rights Reserved.
