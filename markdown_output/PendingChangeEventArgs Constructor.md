Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PendingChangeEventArgs Constructor   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [PendingChangeEventArgs Class](topic890.md) : PendingChangeEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_changesCollection_
    The list to store all changes in.

Glossary Item Box

Creates a new instance of the [PendingChangeEventArgs](topic890.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _changesCollection_ As IList(Of PendingChange) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim changesCollection As IList(Of PendingChange)
     
    Dim instance As New [PendingChangeEventArgs](topic890.md)(changesCollection)  
  
C#|   
---|---  
      
    
    public PendingChangeEventArgs( 
       IList<PendingChange> _changesCollection_
    )  
  
#### Parameters

 _changesCollection_
    The list to store all changes in.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[PendingChangeEventArgs Class](topic890.md)   
[PendingChangeEventArgs Members](topic891.md)


