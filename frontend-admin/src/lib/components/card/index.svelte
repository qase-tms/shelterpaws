<script lang="ts">
</script>

<div class="card">
	<slot />
</div>

<style>
	.card {
		box-shadow: 3px 3px 6px #2222222f;
		background-color: white;
		padding: 24px;

		max-width: var(--max-card-width);

        display: flex;
        flex-direction: var(--direction);
        justify-content: stretch;
        gap: var(--gap);
	}
</style>
