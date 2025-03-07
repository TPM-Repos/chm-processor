Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateState Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxCreateState Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_title_
    The title of the new state.

Glossary Item Box

Creates a transaction which, when committed, will create a state with given title and position. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxCreateState( _
       ByVal _title_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim title As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateState(title)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateState( 
       string _title_
    )  
  
#### Parameters

 _title_
    The title of the new state.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


