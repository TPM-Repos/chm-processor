Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ChangedIndexes Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IndexesChangedEventArgs Class](topic3496.md) : ChangedIndexes Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The original index, before the change. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property ChangedIndexes As IEnumerable(Of ChangedValue(Of Integer))  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IndexesChangedEventArgs](topic3496.md)
    Dim value As IEnumerable(Of ChangedValue(Of Integer))
     
    value = instance.ChangedIndexes  
  
C#|   
---|---  
      
    
    public IEnumerable<ChangedValue<int>> ChangedIndexes {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IndexesChangedEventArgs Class](topic3496.md)   
[IndexesChangedEventArgs Members](topic3497.md)


