Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsRegistering Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [TransactionEventArgs Class](topic1109.md) : IsRegistering Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets whether this transaction is being registered for the first time. As apposed to being run through undo or redo. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property IsRegistering As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TransactionEventArgs](topic1109.md)
    Dim value As Boolean
     
    value = instance.IsRegistering  
  
C#|   
---|---  
      
    
    public bool IsRegistering {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TransactionEventArgs Class](topic1109.md)   
[TransactionEventArgs Members](topic1110.md)


