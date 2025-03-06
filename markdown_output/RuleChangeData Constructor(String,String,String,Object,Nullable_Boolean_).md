![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RuleChangeData Constructor(String,String,String,Object,Nullable<Boolean>)   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5263.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [RuleChangeData Class](topic5254.md) > [RuleChangeData Constructor](topic5260.md) : RuleChangeData Constructor(String,String,String,Object,Nullable<Boolean>)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ruleName_
    The name of the rule.

_formula_
    The formula to apply to the rule.

_comment_
    The comment to apply to the rule.

_value_
    The value to apply to the rule.

_isDynamic_
    Whether the property should be dynamic.

Glossary Item Box

Creates a new instance of the [RuleChangeData](topic5254.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _ruleName_ As String, _
       ByVal _formula_ As String, _
       ByVal _comment_ As String, _
       ByVal _value_ As Object, _
       ByVal _isDynamic_ As Nullable(Of Boolean) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim ruleName As String
    Dim formula As String
    Dim comment As String
    Dim value As Object
    Dim isDynamic As Nullable(Of Boolean)
     
    Dim instance As New [RuleChangeData](topic5254.md)(ruleName, formula, comment, value, isDynamic)  
  
C#|   
---|---  
      
    
    public RuleChangeData( 
       string _ruleName_ ,
       string _formula_ ,
       string _comment_ ,
       object _value_ ,
       Nullable<bool> _isDynamic_
    )  
  
#### Parameters

 _ruleName_
    The name of the rule.
_formula_
    The formula to apply to the rule.
_comment_
    The comment to apply to the rule.
_value_
    The value to apply to the rule.
_isDynamic_
    Whether the property should be dynamic.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[RuleChangeData Class](topic5254.md)   
[RuleChangeData Members](topic5255.md)   
[Overload List](topic5260.md)

©2024 DriveWorks Ltd. All Rights Reserved.
