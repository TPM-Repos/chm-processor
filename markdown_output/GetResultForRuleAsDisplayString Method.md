![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetResultForRuleAsDisplayString Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocument Class](topic4356.md) : GetResultForRuleAsDisplayString Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_results_
    The results from which to retrieve the rule.

_rule_
    The rule for which to retrieve the calculated result.

Glossary Item Box

Gets the specified rule as a string from the calculated results. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Function GetResultForRuleAsDisplayString( _
       ByVal _results_ As [RuleResults](topic11136.md), _
       ByVal _rule_ As [ProjectDocumentRule](topic4399.md) _
    ) As String  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocument](topic4356.md)
    Dim results As [RuleResults](topic11136.md)
    Dim rule As [ProjectDocumentRule](topic4399.md)
    Dim value As String
     
    value = instance.GetResultForRuleAsDisplayString(results, rule)  
  
C#|   
---|---  
      
    
    protected string GetResultForRuleAsDisplayString( 
       [RuleResults](topic11136.md) _results_ ,
       [ProjectDocumentRule](topic4399.md) _rule_
    )  
  
#### Parameters

 _results_
    The results from which to retrieve the rule.
_rule_
    The rule for which to retrieve the calculated result.

#### Return Value

The result of the rule, converted to a string suitable for display.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectDocument Class](topic4356.md)   
[ProjectDocument Members](topic4357.md)


