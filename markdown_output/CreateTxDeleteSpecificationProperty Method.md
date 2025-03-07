Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxDeleteSpecificationProperty Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxDeleteSpecificationProperty Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationProperty_
    The specification property to delete.

Glossary Item Box

Creates a transaction which, when commited, will delete the given specification property. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxDeleteSpecificationProperty( _
       ByVal _specificationProperty_ As [ProjectSpecificationProperty](topic4853.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim specificationProperty As [ProjectSpecificationProperty](topic4853.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxDeleteSpecificationProperty(specificationProperty)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxDeleteSpecificationProperty( 
       [ProjectSpecificationProperty](topic4853.md) _specificationProperty_
    )  
  
#### Parameters

 _specificationProperty_
    The specification property to delete.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


