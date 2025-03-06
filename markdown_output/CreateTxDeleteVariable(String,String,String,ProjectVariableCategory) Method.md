![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxDeleteVariable(String,String,String,ProjectVariableCategory) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13108.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) > [CreateTxDeleteVariable Method](topic13106.md) : CreateTxDeleteVariable(String,String,String,ProjectVariableCategory) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_displayName_
    The display name of the variable to create.

_rule_
    The rule to apply, or a null reference to not apply a comment..

_comment_
    The comment to apply, or a null reference to not apply a comment.

_category_
    The category to apply, or a null reference to not apply a category.

Glossary Item Box

Creates a transaction which, when committed, will create a new variable. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTxDeleteVariable( _
       ByVal _displayName_ As String, _
       ByVal _rule_ As String, _
       ByVal _comment_ As String, _
       ByVal _category_ As [ProjectVariableCategory](topic4983.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim displayName As String
    Dim rule As String
    Dim comment As String
    Dim category As [ProjectVariableCategory](topic4983.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxDeleteVariable(displayName, rule, comment, category)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxDeleteVariable( 
       string _displayName_ ,
       string _rule_ ,
       string _comment_ ,
       [ProjectVariableCategory](topic4983.md) _category_
    )  
  
#### Parameters

 _displayName_
    The display name of the variable to create.
_rule_
    The rule to apply, or a null reference to not apply a comment..
_comment_
    The comment to apply, or a null reference to not apply a comment.
_category_
    The category to apply, or a null reference to not apply a category.

#### Return Value

A transaction which, when executed, will perform the operation.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)   
[Overload List](topic13106.md)

©2024 DriveWorks Ltd. All Rights Reserved.
