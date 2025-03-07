Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IndexesChangedEventArgs Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IndexesChangedEventArgs Class](topic3496.md) : IndexesChangedEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_changedIndexes_
    The original index.

Glossary Item Box

Creates a new instance of the [IndexesChangedEventArgs](topic3496.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _changedIndexes_ As IEnumerable(Of ChangedValue(Of Integer)) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim changedIndexes As IEnumerable(Of ChangedValue(Of Integer))
     
    Dim instance As New [IndexesChangedEventArgs](topic3496.md)(changedIndexes)  
  
C#|   
---|---  
      
    
    public IndexesChangedEventArgs( 
       IEnumerable<ChangedValue<int>> _changedIndexes_
    )  
  
#### Parameters

 _changedIndexes_
    The original index.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IndexesChangedEventArgs Class](topic3496.md)   
[IndexesChangedEventArgs Members](topic3497.md)


