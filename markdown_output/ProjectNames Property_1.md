Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectNames Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [ComponentItemModel Class](topic9662.md) : ProjectNames Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a collection of the names of the projects that this component has been used in. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property ProjectNames As HashSet(Of String)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentItemModel](topic9662.md)
    Dim value As HashSet(Of String)
     
    value = instance.ProjectNames  
  
C#|   
---|---  
      
    
    public HashSet<string> ProjectNames {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentItemModel Class](topic9662.md)   
[ComponentItemModel Members](topic9663.md)


