Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateSnapshot Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Project Class](topic3859.md) : CreateSnapshot Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_snapshotPath_
    The path to create the snapshot at.

Glossary Item Box

Creates a snapshot of the project. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub CreateSnapshot( _
       ByVal _snapshotPath_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Project](topic3859.md)
    Dim snapshotPath As String
     
    instance.CreateSnapshot(snapshotPath)  
  
C#|   
---|---  
      
    
    public void CreateSnapshot( 
       string _snapshotPath_
    )  
  
#### Parameters

 _snapshotPath_
    The path to create the snapshot at.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Project Class](topic3859.md)   
[Project Members](topic3860.md)


