       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ShouldGeneratePreview(IDictionary<String,String>) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4388.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocument Class](topic4356.md) > [ShouldGeneratePreview Method](topic4386.md) : ShouldGeneratePreview(IDictionary<String,String>) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_overriddenRules_
    A dictionary containing overridden rules, where the key is the unique identifier of the rule being overridden, and the value is the new formula.

Glossary Item Box

Determines whether the document should be generated during preview. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function ShouldGeneratePreview( _
       ByVal _overriddenRules_ As IDictionary(Of String,String) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocument](topic4356.md)
    Dim overriddenRules As IDictionary(Of String,String)
    Dim value As Boolean
     
    value = instance.ShouldGeneratePreview(overriddenRules)  
  
C#|   
---|---  
      
    
    public bool ShouldGeneratePreview( 
       IDictionary<string,string> _overriddenRules_
    )  
  
#### Parameters

 _overriddenRules_
    A dictionary containing overridden rules, where the key is the unique identifier of the rule being overridden, and the value is the new formula.

#### Return Value

Returns True if the document should be generated during preview.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDocument Class](topic4356.md)   
[ProjectDocument Members](topic4357.md)   
[Overload List](topic4386.md)

©2024 DriveWorks Ltd. All Rights Reserved.
