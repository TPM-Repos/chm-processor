![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeComponentTaskProperty(ProjectComponent,String,String,Boolean,String,Object,String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic12948.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) > [CreateTxChangeComponentTaskProperty Method](topic12946.md) : CreateTxChangeComponentTaskProperty(ProjectComponent,String,String,Boolean,String,Object,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_component_
    The component that owns the task to change.

_taskName_
    The name of the task that owns the property to change.

_propertyName_
    The name of the property to change.

_isBound_
    True to make the property rule bound, False to make the property static.

_formula_
    The formula to apply to the property (if the property is bound).

_value_
    The value to apply to the property (if the property is not bound).

_comment_
    The comment to apply to the task property.

Glossary Item Box

Creates a new transaction that when executed will change a property on the given [DriveWorks.Components.Tasks.ComponentTask](topic6407.md). 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTxChangeComponentTaskProperty( _
       ByVal _component_ As [ProjectComponent](topic6183.md), _
       ByVal _taskName_ As String, _
       ByVal _propertyName_ As String, _
       ByVal _isBound_ As Boolean, _
       ByVal _formula_ As String, _
       ByVal _value_ As Object, _
       ByVal _comment_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim component As [ProjectComponent](topic6183.md)
    Dim taskName As String
    Dim propertyName As String
    Dim isBound As Boolean
    Dim formula As String
    Dim value As Object
    Dim comment As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeComponentTaskProperty(component, taskName, propertyName, isBound, formula, value, comment)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeComponentTaskProperty( 
       [ProjectComponent](topic6183.md) _component_ ,
       string _taskName_ ,
       string _propertyName_ ,
       bool _isBound_ ,
       string _formula_ ,
       object _value_ ,
       string _comment_
    )  
  
#### Parameters

 _component_
    The component that owns the task to change.
_taskName_
    The name of the task that owns the property to change.
_propertyName_
    The name of the property to change.
_isBound_
    True to make the property rule bound, False to make the property static.
_formula_
    The formula to apply to the property (if the property is bound).
_value_
    The value to apply to the property (if the property is not bound).
_comment_
    The comment to apply to the task property.

#### Return Value

A transaction that when executed will change the property of the [DriveWorks.Components.Tasks.ComponentTask](topic6407.md).

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)   
[Overload List](topic12946.md)

©2024 DriveWorks Ltd. All Rights Reserved.
