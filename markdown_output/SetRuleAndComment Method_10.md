       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetRuleAndComment Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3993.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectCalculationTableRule Class](topic3986.md) : SetRuleAndComment Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_newRule_
    The formula to give this rule.

_newComment_
    The comment to give this rule.

Glossary Item Box

Sets both and rule and comment in one rule revision. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SetRuleAndComment( _
       ByVal _newRule_ As String, _
       ByVal _newComment_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectCalculationTableRule](topic3986.md)
    Dim newRule As String
    Dim newComment As String
     
    instance.SetRuleAndComment(newRule, newComment)  
  
C#|   
---|---  
      
    
    public void SetRuleAndComment( 
       string _newRule_ ,
       string _newComment_
    )  
  
#### Parameters

 _newRule_
    The formula to give this rule.
_newComment_
    The comment to give this rule.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectCalculationTableRule Class](topic3986.md)   
[ProjectCalculationTableRule Members](topic3987.md)

©2024 DriveWorks Ltd. All Rights Reserved.
