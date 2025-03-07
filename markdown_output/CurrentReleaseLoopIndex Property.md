Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CurrentReleaseLoopIndex Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectSpecialVariables Class](topic4782.md) : CurrentReleaseLoopIndex Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the current loop index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride ReadOnly Property CurrentReleaseLoopIndex As Integer  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectSpecialVariables](topic4782.md)
    Dim value As Integer
     
    value = instance.CurrentReleaseLoopIndex  
  
C#|   
---|---  
      
    
    public abstract int CurrentReleaseLoopIndex {get;}  
  
# Remarks

This is only valid during the release process.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectSpecialVariables Class](topic4782.md)   
[ProjectSpecialVariables Members](topic4783.md)


