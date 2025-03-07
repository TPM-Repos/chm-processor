Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ParentId Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleasedComponentReferenceDetails Class](topic6356.md) : ParentId Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The unique id of the parent driven component to which the reference applies. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <DebuggerDisplayAttribute(Value="Guid = {ParentId.ToString("B")}", 
       Name="", 
       Type="", 
       Target=, 
       TargetTypeName="")>
    Public Property ParentId As Guid  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedComponentReferenceDetails](topic6356.md)
    Dim value As Guid
     
    instance.ParentId = value
     
    value = instance.ParentId  
  
C#|   
---|---  
      
    
    [DebuggerDisplayAttribute(Value="Guid = {ParentId.ToString("B")}", 
       Name="", 
       Type="", 
       Target=, 
       TargetTypeName="")]
    public Guid ParentId {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedComponentReferenceDetails Class](topic6356.md)   
[ReleasedComponentReferenceDetails Members](topic6357.md)


