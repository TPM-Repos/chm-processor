Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OriginalVersion Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Project Class](topic3859.md) : OriginalVersion Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the version of the project when it was loaded from file. This is not the current version, as it could have been upgraded since it was loaded. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property OriginalVersion As Version  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Project](topic3859.md)
    Dim value As Version
     
    value = instance.OriginalVersion  
  
C#|   
---|---  
      
    
    public Version OriginalVersion {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Project Class](topic3859.md)   
[Project Members](topic3860.md)


