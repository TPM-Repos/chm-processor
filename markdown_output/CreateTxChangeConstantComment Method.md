Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeConstantComment Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeConstantComment Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_constant_
    The constant to modify.

_newComment_
    The new comment to assign to the constant.

Glossary Item Box

Creates a transaction which, when committed, will change the comment of the specified constant. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeConstantComment( _
       ByVal _constant_ As [ProjectConstant](topic4171.md), _
       ByVal _newComment_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim constant As [ProjectConstant](topic4171.md)
    Dim newComment As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeConstantComment(constant, newComment)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeConstantComment( 
       [ProjectConstant](topic4171.md) _constant_ ,
       string _newComment_
    )  
  
#### Parameters

 _constant_
    The constant to modify.
_newComment_
    The new comment to assign to the constant.

#### Return Value

A transaction which, when executed, will perform the operation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


