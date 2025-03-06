![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeComponentTaskPropertyExtendedValue Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeComponentTaskPropertyExtendedValue Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_component_
    The component the task belongs to.

_task_
    The task the property belongs to.

_propertyName_
    The name of the property to change the extended value of.

_isExtended_
    True to make the property extended.

Glossary Item Box

Creates a new transaction that when executed will change the extended value of the given task property. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeComponentTaskPropertyExtendedValue( _
       ByVal _component_ As [ProjectComponent](topic6183.md), _
       ByVal _task_ As [ComponentTask](topic6407.md), _
       ByVal _propertyName_ As String, _
       ByVal _isExtended_ As Boolean _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim component As [ProjectComponent](topic6183.md)
    Dim task As [ComponentTask](topic6407.md)
    Dim propertyName As String
    Dim isExtended As Boolean
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeComponentTaskPropertyExtendedValue(component, task, propertyName, isExtended)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeComponentTaskPropertyExtendedValue( 
       [ProjectComponent](topic6183.md) _component_ ,
       [ComponentTask](topic6407.md) _task_ ,
       string _propertyName_ ,
       bool _isExtended_
    )  
  
#### Parameters

 _component_
    The component the task belongs to.
_task_
    The task the property belongs to.
_propertyName_
    The name of the property to change the extended value of.
_isExtended_
    True to make the property extended.

#### Return Value

A new transaction that when executed will change the extended property of a component task property.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


