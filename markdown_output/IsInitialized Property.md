Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsInitialized Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDataTable Class](topic4282.md) : IsInitialized Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets whether the table has been initialized. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property IsInitialized As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDataTable](topic4282.md)
    Dim value As Boolean
     
    value = instance.IsInitialized  
  
C#|   
---|---  
      
    
    public bool IsInitialized {get;}  
  
# Remarks

When a table is first created, it is not attached to a project and some functionality of the table may not available.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDataTable Class](topic4282.md)   
[ProjectDataTable Members](topic4283.md)


