Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeSpecificationFlowCustomization Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeSpecificationFlowCustomization Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_customize_
    False to restore the default specification flow, true to allow changes.

Glossary Item Box

Creates a transaction which, when commited, will Change the specification flow's customization to either customized or defualt. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeSpecificationFlowCustomization( _
       ByVal _customize_ As Boolean _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim customize As Boolean
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeSpecificationFlowCustomization(customize)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeSpecificationFlowCustomization( 
       bool _customize_
    )  
  
#### Parameters

 _customize_
    False to restore the default specification flow, true to allow changes.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


