Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Id Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleasedComponentReferenceDetails Class](topic6356.md) : Id Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the unique id of the reference. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <DebuggerDisplayAttribute(Value="Guid = {Id.ToString("B")}", 
       Name="", 
       Type="", 
       Target=, 
       TargetTypeName="")>
    Public Property Id As Guid  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedComponentReferenceDetails](topic6356.md)
    Dim value As Guid
     
    instance.Id = value
     
    value = instance.Id  
  
C#|   
---|---  
      
    
    [DebuggerDisplayAttribute(Value="Guid = {Id.ToString("B")}", 
       Name="", 
       Type="", 
       Target=, 
       TargetTypeName="")]
    public Guid Id {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedComponentReferenceDetails Class](topic6356.md)   
[ReleasedComponentReferenceDetails Members](topic6357.md)


