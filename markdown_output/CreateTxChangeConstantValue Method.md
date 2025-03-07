Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeConstantValue Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeConstantValue Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_constant_
    The constant to modify.

_newValue_
    The new value to assign to the constant.

Glossary Item Box

Creates a transaction which, when committed, will change the value of the specified constant. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeConstantValue( _
       ByVal _constant_ As [ProjectConstant](topic4171.md), _
       ByVal _newValue_ As Object _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim constant As [ProjectConstant](topic4171.md)
    Dim newValue As Object
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeConstantValue(constant, newValue)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeConstantValue( 
       [ProjectConstant](topic4171.md) _constant_ ,
       object _newValue_
    )  
  
#### Parameters

 _constant_
    The constant to modify.
_newValue_
    The new value to assign to the constant.

#### Return Value

A transaction which, when executed, will perform the operation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


