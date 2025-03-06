![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GenericRuleWithCustomName Constructor(String,String,String)   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6070.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Abstractions Namespace](topic5939.md) > [GenericRuleWithCustomName Class](topic6063.md) > [GenericRuleWithCustomName Constructor](topic6069.md) : GenericRuleWithCustomName Constructor(String,String,String)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_customAndDisplayName_
    The custom name of the rule to return from MyName calls, as well as its display name.

_formula_
    The formula which defines the rule.

_comment_
    The comment which describes the operation of the rule.

Glossary Item Box

Initializes a new instance of the [GenericRuleWithCustomName](topic6063.md) type. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _customAndDisplayName_ As String, _
       ByVal _formula_ As String, _
       ByVal _comment_ As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim customAndDisplayName As String
    Dim formula As String
    Dim comment As String
     
    Dim instance As New [GenericRuleWithCustomName](topic6063.md)(customAndDisplayName, formula, comment)  
  
C#|   
---|---  
      
    
    public GenericRuleWithCustomName( 
       string _customAndDisplayName_ ,
       string _formula_ ,
       string _comment_
    )  
  
#### Parameters

 _customAndDisplayName_
    The custom name of the rule to return from MyName calls, as well as its display name.
_formula_
    The formula which defines the rule.
_comment_
    The comment which describes the operation of the rule.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GenericRuleWithCustomName Class](topic6063.md)   
[GenericRuleWithCustomName Members](topic6064.md)   
[Overload List](topic6069.md)

©2024 DriveWorks Ltd. All Rights Reserved.
