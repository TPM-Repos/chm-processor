Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxRecreateFormControl(String,String,String,Int32) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) > [CreateTxRecreateFormControl Method](topic13118.md) : CreateTxRecreateFormControl(String,String,String,Int32) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_formName_
    The name of the form to create the controls on.

_parentName_
    The name of the parent control to create the controls in.

_controlSerializationData_
    The pasted serialized text for the controls.

_insertIndex_
    The control index of which to insert the controls at.

Glossary Item Box

Creates a transaction that create new controls from the given serialized text. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTxRecreateFormControl( _
       ByVal _formName_ As String, _
       ByVal _parentName_ As String, _
       ByVal _controlSerializationData_ As String, _
       ByVal _insertIndex_ As Integer _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim formName As String
    Dim parentName As String
    Dim controlSerializationData As String
    Dim insertIndex As Integer
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxRecreateFormControl(formName, parentName, controlSerializationData, insertIndex)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxRecreateFormControl( 
       string _formName_ ,
       string _parentName_ ,
       string _controlSerializationData_ ,
       int _insertIndex_
    )  
  
#### Parameters

 _formName_
    The name of the form to create the controls on.
_parentName_
    The name of the parent control to create the controls in.
_controlSerializationData_
    The pasted serialized text for the controls.
_insertIndex_
    The control index of which to insert the controls at.

#### Return Value

A transaction

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)   
[Overload List](topic13118.md)


