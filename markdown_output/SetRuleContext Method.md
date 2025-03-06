![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetRuleContext Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4382.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocument Class](topic4356.md) : SetRuleContext Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_rule_
    The rule to set the context of.

_context_
    The context to give the rule.

Glossary Item Box

Sets a rule context that will be use by the Titan rule engine when evaluating the rule. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Sub SetRuleContext( _
       ByVal _rule_ As [ProjectDocumentRule](topic4399.md), _
       ByVal _context_ As Object _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocument](topic4356.md)
    Dim rule As [ProjectDocumentRule](topic4399.md)
    Dim context As Object
     
    instance.SetRuleContext(rule, context)  
  
C#|   
---|---  
      
    
    protected void SetRuleContext( 
       [ProjectDocumentRule](topic4399.md) _rule_ ,
       object _context_
    )  
  
#### Parameters

 _rule_
    The rule to set the context of.
_context_
    The context to give the rule.

# ![](dotnetimages/collapse.gif)Remarks

This is typically used to provide custom MyName() values, or relative rule resolvers.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectDocument Class](topic4356.md)   
[ProjectDocument Members](topic4357.md)

©2024 DriveWorks Ltd. All Rights Reserved.
