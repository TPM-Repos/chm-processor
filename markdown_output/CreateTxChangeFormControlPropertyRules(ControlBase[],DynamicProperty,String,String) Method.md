![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeFormControlPropertyRules(ControlBase[],DynamicProperty,String,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeFormControlPropertyRules(ControlBase[],DynamicProperty,String,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_controls_
    The controls to change.

_prop_
    The dynamic property to change on the named controls.

_newRule_
    The new rule to apply to the property.

_newComment_
    The new comment to apply to the property.

Glossary Item Box

Changes the given property on the specified controls to the provided value. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeFormControlPropertyRules( _
       ByVal _controls_() As [ControlBase](topic7698.md), _
       ByVal _prop_ As [DynamicProperty](topic9398.md), _
       ByVal _newRule_ As String, _
       ByVal _newComment_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim controls() As [ControlBase](topic7698.md)
    Dim prop As [DynamicProperty](topic9398.md)
    Dim newRule As String
    Dim newComment As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeFormControlPropertyRules(controls, prop, newRule, newComment)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeFormControlPropertyRules( 
       [ControlBase](topic7698.md)[] _controls_ ,
       [DynamicProperty](topic9398.md) _prop_ ,
       string _newRule_ ,
       string _newComment_
    )  
  
#### Parameters

 _controls_
    The controls to change.
_prop_
    The dynamic property to change on the named controls.
_newRule_
    The new rule to apply to the property.
_newComment_
    The new comment to apply to the property.

#### Return Value

A transaction.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


