Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxUndoDeleteOperation Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxUndoDeleteOperation Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sourceStateTitle_
    The title of the source state.

_name_
    The name of the operation to re-create.

_title_
    The title of the operation.

_conditions_
    The conditions of the operation.

_teams_
    The teams of the operation.

_taskSequence_
    The tasks of the operation.

Glossary Item Box

Creates a transaction which, when committed, will undo a deletion of a operation with all its specified parameters. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxUndoDeleteOperation( _
       ByVal _sourceStateTitle_ As String, _
       ByVal _name_ As String, _
       ByVal _title_ As String, _
       ByVal _conditions_ As [Conditions](topic10865.md), _
       ByVal _teams_ As [Teams](topic11737.md), _
       ByVal _taskSequence_ As [TaskSequence](topic11713.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim sourceStateTitle As String
    Dim name As String
    Dim title As String
    Dim conditions As [Conditions](topic10865.md)
    Dim teams As [Teams](topic11737.md)
    Dim taskSequence As [TaskSequence](topic11713.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxUndoDeleteOperation(sourceStateTitle, name, title, conditions, teams, taskSequence)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxUndoDeleteOperation( 
       string _sourceStateTitle_ ,
       string _name_ ,
       string _title_ ,
       [Conditions](topic10865.md) _conditions_ ,
       [Teams](topic11737.md) _teams_ ,
       [TaskSequence](topic11713.md) _taskSequence_
    )  
  
#### Parameters

 _sourceStateTitle_
    The title of the source state.
_name_
    The name of the operation to re-create.
_title_
    The title of the operation.
_conditions_
    The conditions of the operation.
_teams_
    The teams of the operation.
_taskSequence_
    The tasks of the operation.

# Remarks

Parameters can be set to nothing for no prefernce.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


