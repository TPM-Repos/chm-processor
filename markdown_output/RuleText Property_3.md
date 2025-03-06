       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RuleText Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardTasks Namespace](topic11896.md) > [EvaluateRuleValueTask Class](topic12258.md) : RuleText Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the rule that will be evaluated once, then have its result evaluated again. The final result of which is stored in the target constant, specified by [ConstantName](topic12267.md). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property RuleText As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [EvaluateRuleValueTask](topic12258.md)
    Dim value As String
     
    instance.RuleText = value
     
    value = instance.RuleText  
  
C#|   
---|---  
      
    
    public string RuleText {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[EvaluateRuleValueTask Class](topic12258.md)   
[EvaluateRuleValueTask Members](topic12259.md)


