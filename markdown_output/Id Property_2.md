Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Id Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) > [TeamDetails Class](topic10703.md) : Id Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the unique identifier of the team. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <DebuggerDisplayAttribute(Value="Guid = {Id.ToString("B")}", 
       Name="", 
       Type="", 
       Target=, 
       TargetTypeName="")>
    Public ReadOnly Property Id As Guid  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TeamDetails](topic10703.md)
    Dim value As Guid
     
    value = instance.Id  
  
C#|   
---|---  
      
    
    [DebuggerDisplayAttribute(Value="Guid = {Id.ToString("B")}", 
       Name="", 
       Type="", 
       Target=, 
       TargetTypeName="")]
    public Guid Id {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TeamDetails Class](topic10703.md)   
[TeamDetails Members](topic10704.md)


