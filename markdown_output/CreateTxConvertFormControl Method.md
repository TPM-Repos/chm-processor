![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxConvertFormControl Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13025.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxConvertFormControl Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_form_
    The form that parents the source control.

_sourceControl_
    The control to convert.

_targetType_
    The type of control to convert the source control to.

Glossary Item Box

Creates a transaction that will convert the given control into the target control type specified. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxConvertFormControl( _
       ByVal _form_ As [Form](topic8086.md), _
       ByVal _sourceControl_ As [ControlBase](topic7698.md), _
       ByVal _targetType_ As Type _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim form As [Form](topic8086.md)
    Dim sourceControl As [ControlBase](topic7698.md)
    Dim targetType As Type
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxConvertFormControl(form, sourceControl, targetType)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxConvertFormControl( 
       [Form](topic8086.md) _form_ ,
       [ControlBase](topic7698.md) _sourceControl_ ,
       Type _targetType_
    )  
  
#### Parameters

 _form_
    The form that parents the source control.
_sourceControl_
    The control to convert.
_targetType_
    The type of control to convert the source control to.

#### Return Value

A transaction

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)

©2024 DriveWorks Ltd. All Rights Reserved.
