![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeFormControlPropertyValues(ControlBase[],DynamicProperty,Object) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic12974.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeFormControlPropertyValues(ControlBase[],DynamicProperty,Object) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_controls_
    The controls to change.

_prop_
    The dynamic property to change on the named controls.

_newValue_
    The new value to apply to the property.

Glossary Item Box

Changes the given property on the specified controls to the provided value. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeFormControlPropertyValues( _
       ByVal _controls_() As [ControlBase](topic7698.md), _
       ByVal _prop_ As [DynamicProperty](topic9398.md), _
       ByVal _newValue_ As Object _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim controls() As [ControlBase](topic7698.md)
    Dim prop As [DynamicProperty](topic9398.md)
    Dim newValue As Object
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeFormControlPropertyValues(controls, prop, newValue)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeFormControlPropertyValues( 
       [ControlBase](topic7698.md)[] _controls_ ,
       [DynamicProperty](topic9398.md) _prop_ ,
       object _newValue_
    )  
  
#### Parameters

 _controls_
    The controls to change.
_prop_
    The dynamic property to change on the named controls.
_newValue_
    The new value to apply to the property.

#### Return Value

A transaction.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)

©2024 DriveWorks Ltd. All Rights Reserved.
