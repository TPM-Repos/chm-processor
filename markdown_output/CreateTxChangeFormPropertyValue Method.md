Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeFormPropertyValue Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeFormPropertyValue Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_form_
    The form that we want to change properties on.

_prop_
    The property to change on the form.

_newValue_
    The new value to apply to the property.

Glossary Item Box

Changes the given property on the specified form to the provided value. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeFormPropertyValue( _
       ByVal _form_ As [Form](topic8086.md), _
       ByVal _prop_ As [DynamicProperty](topic9398.md), _
       ByVal _newValue_ As Object _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim form As [Form](topic8086.md)
    Dim prop As [DynamicProperty](topic9398.md)
    Dim newValue As Object
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeFormPropertyValue(form, prop, newValue)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeFormPropertyValue( 
       [Form](topic8086.md) _form_ ,
       [DynamicProperty](topic9398.md) _prop_ ,
       object _newValue_
    )  
  
#### Parameters

 _form_
    The form that we want to change properties on.
_prop_
    The property to change on the form.
_newValue_
    The new value to apply to the property.

#### Return Value

A transaction

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


