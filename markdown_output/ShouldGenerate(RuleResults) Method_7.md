       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ShouldGenerate(RuleResults) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5719.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [TriggeredAction Class](topic5708.md) > [ShouldGenerate Method](topic5718.md) : ShouldGenerate(RuleResults) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_results_
    The calculated rule results for the document.

Glossary Item Box

Determines whether the document should be generated. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Overrides NotOverridable Function ShouldGenerate( _
       ByVal _results_ As [RuleResults](topic11136.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TriggeredAction](topic5708.md)
    Dim results As [RuleResults](topic11136.md)
    Dim value As Boolean
     
    value = instance.ShouldGenerate(results)  
  
C#|   
---|---  
      
    
    public override bool ShouldGenerate( 
       [RuleResults](topic11136.md) _results_
    )  
  
#### Parameters

 _results_
    The calculated rule results for the document.

#### Return Value

Returns True if the document should be generated.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TriggeredAction Class](topic5708.md)   
[TriggeredAction Members](topic5709.md)   
[Overload List](topic5718.md)

©2024 DriveWorks Ltd. All Rights Reserved.
