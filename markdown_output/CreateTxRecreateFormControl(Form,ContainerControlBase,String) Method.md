Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxRecreateFormControl(Form,ContainerControlBase,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) > [CreateTxRecreateFormControl Method](topic13118.md) : CreateTxRecreateFormControl(Form,ContainerControlBase,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_form_
    The form to create the controls on.

_parent_
    The parent control to create the controls in.

_controlSerializationData_
    The pasted serialized text for the controls.

Glossary Item Box

Creates a transaction Create new controls from the given serialized text. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTxRecreateFormControl( _
       ByVal _form_ As [Form](topic8086.md), _
       ByVal _parent_ As [ContainerControlBase](topic7684.md), _
       ByVal _controlSerializationData_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim form As [Form](topic8086.md)
    Dim parent As [ContainerControlBase](topic7684.md)
    Dim controlSerializationData As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxRecreateFormControl(form, parent, controlSerializationData)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxRecreateFormControl( 
       [Form](topic8086.md) _form_ ,
       [ContainerControlBase](topic7684.md) _parent_ ,
       string _controlSerializationData_
    )  
  
#### Parameters

 _form_
    The form to create the controls on.
_parent_
    The parent control to create the controls in.
_controlSerializationData_
    The pasted serialized text for the controls.

#### Return Value

A transaction

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)   
[Overload List](topic13118.md)


