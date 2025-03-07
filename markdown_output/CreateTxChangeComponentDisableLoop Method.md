Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeComponentDisableLoop Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeComponentDisableLoop Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_component_
    The component to change.

Glossary Item Box

Creates a new transaction that when executed will disable the release loop for the given component. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeComponentDisableLoop( _
       ByVal _component_ As [ProjectComponent](topic6183.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim component As [ProjectComponent](topic6183.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeComponentDisableLoop(component)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeComponentDisableLoop( 
       [ProjectComponent](topic6183.md) _component_
    )  
  
#### Parameters

 _component_
    The component to change.

#### Return Value

A new transaction that when executed will disable the release loop for the given component.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


