Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeleteFileReferenceByTargetPath Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReleasedComponents Class](topic3238.md) : DeleteFileReferenceByTargetPath Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentTargetPath_
    The full path to the released component to delete.

Glossary Item Box

Deletes a released component and references to it from the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub DeleteFileReferenceByTargetPath( _
       ByVal _componentTargetPath_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupReleasedComponents](topic3238.md)
    Dim componentTargetPath As String
     
    instance.DeleteFileReferenceByTargetPath(componentTargetPath)  
  
C#|   
---|---  
      
    
    public void DeleteFileReferenceByTargetPath( 
       string _componentTargetPath_
    )  
  
#### Parameters

 _componentTargetPath_
    The full path to the released component to delete.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[GroupReleasedComponents Members](topic3239.md)


