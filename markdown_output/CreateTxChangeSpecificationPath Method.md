Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeSpecificationPath Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeSpecificationPath Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_newRule_
    The new rule to set.

_newComment_
    The new comment.

Glossary Item Box

Creates a transaction which, when committed, will update the specification path's special variable with the given values. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeSpecificationPath( _
       ByVal _newRule_ As String, _
       ByVal _newComment_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim newRule As String
    Dim newComment As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeSpecificationPath(newRule, newComment)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeSpecificationPath( 
       string _newRule_ ,
       string _newComment_
    )  
  
#### Parameters

 _newRule_
    The new rule to set.
_newComment_
    The new comment.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


