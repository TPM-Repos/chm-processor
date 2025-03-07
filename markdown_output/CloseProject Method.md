Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CloseProject Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IProjectService Interface](topic382.md) : CloseProject Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Closes the active project without saving it. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub CloseProject()   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IProjectService](topic382.md)
     
    instance.CloseProject()  
  
C#|   
---|---  
      
    
    void CloseProject()  
  
# Exceptions

Exception| Description  
---|---  
System.InvalidOperationException| The implementation does not support projects being closed by 3rd party code.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IProjectService Interface](topic382.md)   
[IProjectService Members](topic383.md)


