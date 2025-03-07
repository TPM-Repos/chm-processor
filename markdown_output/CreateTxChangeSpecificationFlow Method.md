Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeSpecificationFlow Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeSpecificationFlow Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_newSpecificationFlow_
    Specification flow as XML.

Glossary Item Box

Creates a transaction which, when commited, will change the specification flow to the given data. This will wipe the current flow. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeSpecificationFlow( _
       ByVal _newSpecificationFlow_ As XElement _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim newSpecificationFlow As XElement
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeSpecificationFlow(newSpecificationFlow)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeSpecificationFlow( 
       XElement _newSpecificationFlow_
    )  
  
#### Parameters

 _newSpecificationFlow_
    Specification flow as XML.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


