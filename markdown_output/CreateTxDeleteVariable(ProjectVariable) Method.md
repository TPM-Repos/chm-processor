Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxDeleteVariable(ProjectVariable) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) > [CreateTxDeleteVariable Method](topic13106.md) : CreateTxDeleteVariable(ProjectVariable) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_variable_
    The variable to delete.

Glossary Item Box

Creates a transaction which, when committed, will delete the specified variable 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTxDeleteVariable( _
       ByVal _variable_ As [ProjectVariable](topic4927.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim variable As [ProjectVariable](topic4927.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxDeleteVariable(variable)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxDeleteVariable( 
       [ProjectVariable](topic4927.md) _variable_
    )  
  
#### Parameters

 _variable_
    The variable to delete.

#### Return Value

A transaction which, when executed, will perform the operation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)   
[Overload List](topic13106.md)


