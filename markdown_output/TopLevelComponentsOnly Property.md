TopLevelComponentsOnly Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [CopyGroupOptions Class](topic9736.md) : TopLevelComponentsOnly Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Whether or not the copied components are component sets. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property TopLevelComponentsOnly As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CopyGroupOptions](topic9736.md)
    Dim value As Boolean
     
    instance.TopLevelComponentsOnly = value
     
    value = instance.TopLevelComponentsOnly  
  
C#|   
---|---  
      
    
    public bool TopLevelComponentsOnly {get; set;}  
  
# Remarks

This cannot be true while [AutoSelectComponentsFromSelectedProjects](topic9743.md) is true.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CopyGroupOptions Class](topic9736.md)   
[CopyGroupOptions Members](topic9737.md)


