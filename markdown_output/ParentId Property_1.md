Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ParentId Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReadOnlyReleasedComponentReferenceDetails Class](topic6239.md) : ParentId Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the unique id of the parent driven component to which the reference applies. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <DebuggerDisplayAttribute(Value="Guid = {ParentId.ToString("B")}", 
       Name="", 
       Type="", 
       Target=, 
       TargetTypeName="")>
    Public ReadOnly Property ParentId As Guid  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReadOnlyReleasedComponentReferenceDetails](topic6239.md)
    Dim value As Guid
     
    value = instance.ParentId  
  
C#|   
---|---  
      
    
    [DebuggerDisplayAttribute(Value="Guid = {ParentId.ToString("B")}", 
       Name="", 
       Type="", 
       Target=, 
       TargetTypeName="")]
    public Guid ParentId {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReadOnlyReleasedComponentReferenceDetails Class](topic6239.md)   
[ReadOnlyReleasedComponentReferenceDetails Members](topic6240.md)


