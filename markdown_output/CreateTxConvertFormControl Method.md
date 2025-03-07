Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxConvertFormControl Method   
  
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

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxConvertFormControl( _
       ByVal _form_ As [Form](topic8086.md), _
       ByVal _sourceControl_ As [ControlBase](topic7698.md), _
       ByVal _targetType_ As Type _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


