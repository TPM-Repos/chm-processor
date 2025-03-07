Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxDeleteConstant Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxDeleteConstant Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_constant_
    The constant to be deleted.

Glossary Item Box

Creates a transaction which, when committed, will delete the specified constant. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxDeleteConstant( _
       ByVal _constant_ As [ProjectConstant](topic4171.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim constant As [ProjectConstant](topic4171.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxDeleteConstant(constant)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxDeleteConstant( 
       [ProjectConstant](topic4171.md) _constant_
    )  
  
#### Parameters

 _constant_
    The constant to be deleted.

#### Return Value

A transaction which, when executed, will perform the operation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


