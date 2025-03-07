Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxRestoreChildSpecificationList Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxRestoreChildSpecificationList Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_childSpecDefinition_
    The child specification list to create the backup transaction for.

Glossary Item Box

Creates a new transaction that when executed will restore the state of the given child specification list to when this transaction was created. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxRestoreChildSpecificationList( _
       ByVal _childSpecDefinition_ As [ProjectChildSpecificationDef](topic4019.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim childSpecDefinition As [ProjectChildSpecificationDef](topic4019.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxRestoreChildSpecificationList(childSpecDefinition)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxRestoreChildSpecificationList( 
       [ProjectChildSpecificationDef](topic4019.md) _childSpecDefinition_
    )  
  
#### Parameters

 _childSpecDefinition_
    The child specification list to create the backup transaction for.

# Remarks

This is a backup transaction.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


