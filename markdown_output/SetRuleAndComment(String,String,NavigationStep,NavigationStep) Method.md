       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetRuleAndComment(String,String,NavigationStep,NavigationStep) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10135.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) > [DecisionNavigationStep Class](topic10125.md) > [SetRuleAndComment Method](topic10133.md) : SetRuleAndComment(String,String,NavigationStep,NavigationStep) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_newRule_
    The rule to evaluate.

_newComment_
    The comment for the rule.

_stepIfTrue_
    The step to be shown if the condition evaluates to true.

_stepIfFalse_
    The step to be shown if the condition evaluates to false.

Glossary Item Box

Sets the rule and the comment for the Decision Step. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Sub SetRuleAndComment( _
       ByVal _newRule_ As String, _
       ByVal _newComment_ As String, _
       ByVal _stepIfTrue_ As [NavigationStep](topic10175.md), _
       ByVal _stepIfFalse_ As [NavigationStep](topic10175.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DecisionNavigationStep](topic10125.md)
    Dim newRule As String
    Dim newComment As String
    Dim stepIfTrue As [NavigationStep](topic10175.md)
    Dim stepIfFalse As [NavigationStep](topic10175.md)
     
    instance.SetRuleAndComment(newRule, newComment, stepIfTrue, stepIfFalse)  
  
C#|   
---|---  
      
    
    public void SetRuleAndComment( 
       string _newRule_ ,
       string _newComment_ ,
       [NavigationStep](topic10175.md) _stepIfTrue_ ,
       [NavigationStep](topic10175.md) _stepIfFalse_
    )  
  
#### Parameters

 _newRule_
    The rule to evaluate.
_newComment_
    The comment for the rule.
_stepIfTrue_
    The step to be shown if the condition evaluates to true.
_stepIfFalse_
    The step to be shown if the condition evaluates to false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DecisionNavigationStep Class](topic10125.md)   
[DecisionNavigationStep Members](topic10126.md)   
[Overload List](topic10133.md)

©2024 DriveWorks Ltd. All Rights Reserved.
