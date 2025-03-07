Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxDeleteProjectComponentSet Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxDeleteProjectComponentSet Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentSet_
    The component set to delete.

Glossary Item Box

Creates a transaction that will delete the specified component set. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxDeleteProjectComponentSet( _
       ByVal _componentSet_ As [ProjectComponentSet](topic4106.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim componentSet As [ProjectComponentSet](topic4106.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxDeleteProjectComponentSet(componentSet)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxDeleteProjectComponentSet( 
       [ProjectComponentSet](topic4106.md) _componentSet_
    )  
  
#### Parameters

 _componentSet_
    The component set to delete.

#### Return Value

A transaction that will perform the operation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


