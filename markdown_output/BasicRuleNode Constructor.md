![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BasicRuleNode Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10564.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Rules Namespace](topic10510.md) > [BasicRuleNode Class](topic10558.md) : BasicRuleNode Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_text_
    The inner text of the rule node.

_outerText_
    The outer text of the rule node.

_ruleText_
    The full text of the owning rule that this node is part of.

_nodeType_
    The type for this rule node.

_startIndex_
    The start index of the first character of the inner text of this node.

_endIndex_
    The end index of the last character of the inner text of this node.

_outerStartIndex_
    The start index of the first character of the outer text of this node.

_outerEndIndex_
    The end index of the last character of the outer text of this node.

_children_
    A collection of children for this node (can be empty).

Glossary Item Box

Creates a new instance of the [BasicRuleNode](topic10558.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _text_ As String, _
       ByVal _outerText_ As String, _
       ByVal _ruleText_ As String, _
       ByVal _nodeType_ As [RuleNodeType](topic10556.md), _
       ByVal _startIndex_ As Integer, _
       ByVal _endIndex_ As Integer, _
       ByVal _outerStartIndex_ As Integer, _
       ByVal _outerEndIndex_ As Integer, _
       ByVal _children_() As [IRuleNode](topic10542.md) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim text As String
    Dim outerText As String
    Dim ruleText As String
    Dim nodeType As [RuleNodeType](topic10556.md)
    Dim startIndex As Integer
    Dim endIndex As Integer
    Dim outerStartIndex As Integer
    Dim outerEndIndex As Integer
    Dim children() As [IRuleNode](topic10542.md)
     
    Dim instance As New [BasicRuleNode](topic10558.md)(text, outerText, ruleText, nodeType, startIndex, endIndex, outerStartIndex, outerEndIndex, children)  
  
C#|   
---|---  
      
    
    public BasicRuleNode( 
       string _text_ ,
       string _outerText_ ,
       string _ruleText_ ,
       [RuleNodeType](topic10556.md) _nodeType_ ,
       int _startIndex_ ,
       int _endIndex_ ,
       int _outerStartIndex_ ,
       int _outerEndIndex_ ,
       [IRuleNode](topic10542.md)[] _children_
    )  
  
#### Parameters

 _text_
    The inner text of the rule node.
_outerText_
    The outer text of the rule node.
_ruleText_
    The full text of the owning rule that this node is part of.
_nodeType_
    The type for this rule node.
_startIndex_
    The start index of the first character of the inner text of this node.
_endIndex_
    The end index of the last character of the inner text of this node.
_outerStartIndex_
    The start index of the first character of the outer text of this node.
_outerEndIndex_
    The end index of the last character of the outer text of this node.
_children_
    A collection of children for this node (can be empty).

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[BasicRuleNode Class](topic10558.md)   
[BasicRuleNode Members](topic10559.md)

©2024 DriveWorks Ltd. All Rights Reserved.
